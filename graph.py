import glob
import os
import tomllib
import sys
import matplotlib.pyplot as plt
import tomli_w

from matplotlib import font_manager as fm, rcParams

fontFile = os.path.join(os.path.dirname(sys.argv[0]), "Montserrat.ttf")
print(fontFile)
prop = fm.FontProperties(fname=fontFile)


class Plot:
    def __init__(self, dataX, dataY, config):
        self.dataX = dataX
        self.dataY = dataY
        self.config = config


class Graph:

    @classmethod
    def parse(cls, folder):
        files = glob.glob(os.path.join(folder, "*.csv"))
        plots = []

        graph_config = {
            "title": os.path.basename(folder),
            "axes": {
                "X": {
                    "label": "Temps [ms]",
                    "range": []
                },
                "Y": {
                    "label": "Potentiel [V]",
                    "range": []
                }
            }

        }
        cfg_file = os.path.join(folder, "config.toml")
        if os.path.exists(cfg_file):
            with open(cfg_file, mode="rb") as cfg:
                graph_config = tomllib.load(cfg)
        else:
            with open(cfg_file, "w") as cfg:
                data = tomli_w.dumps(graph_config)
                cfg.write(data)

        for file in files:
            with open(file) as f:
                content = f.readlines()
                dataXA_local = []
                dataXB_local = []
                dataYA_local = []
                dataYB_local = []
                for line in content:
                    try:
                        separator = ";"
                        if "\t" in line:
                            separator = "\t"
                            
                        items = [i.replace(",", ".") for i in line.split(separator)]
                        t, a, b = [float(item) for item in items]
                        dataXA_local.append(t)
                        dataXB_local.append(t)
                        dataYA_local.append(a)
                        dataYB_local.append(b)

                    except:
                        continue
                dataXA_local = list(map(lambda t: t - dataXA_local[0], dataXA_local))
                dataXB_local = list(map(lambda t: t - dataXB_local[0], dataXB_local))
                configfile, _ = os.path.splitext(file)
                configfile += ".toml"
                if os.path.exists(configfile):
                    with open(configfile, mode="rb") as cfg:
                        print(configfile)
                        config = tomllib.load(cfg)
                else:
                    config = {
                        'A': {
                            'enabled': True,
                            'offset': 0,
                            'label': 'A',
                            'color': 'red'

                        },
                        'B': {
                            'enabled': True,
                            'offset': 0,
                            'label': 'B',
                            'color': 'blue'
                        }

                    }
                    with open(configfile, "w") as cfg:
                        data = tomli_w.dumps(config)
                        print("write")
                        cfg.write(data)
                if config['A']['enabled']:
                    plots.append(Plot(dataXA_local, dataYA_local, config['A']))
                if config['B']['enabled']:
                    plots.append(Plot(dataXB_local, dataYB_local, config['B']))

        return Graph(plots, graph_config)

    def __init__(self, plots, config):
        self.plots = plots
        self.config = config

    def plot(self, show=False):
        plt.figure(figsize=(10, 6))
        for plot in self.plots:
            plt.plot(plot.dataX, plot.dataY, label=plot.config["label"], color=plot.config["color"])

        plt.legend(prop=prop)
        plt.title(self.config["title"], fontproperties=prop, fontsize=16)
        plt.xlabel(self.config["axes"]["X"]["label"], fontproperties=prop)
        plt.ylabel(self.config["axes"]["Y"]["label"], fontproperties=prop)
        for ax in ["X","Y"]:
            if self.config["axes"][ax]["range"]:
                if ax == "X":
                    plt.xlim(self.config["axes"][ax]["range"])
                else:
                    plt.ylim(self.config["axes"][ax]["range"])

        plt.show()
        plt.savefig(os.path.join(sys.argv[1], "plot.png"))

