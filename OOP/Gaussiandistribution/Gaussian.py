import math
import matplotlib.pyplot as plt


class Gaussian:
    """
    Gaussian distribution class for calculating and visualizing Gaussian distribution

    Attributes includes:
        mean (float)
        stdev (float)
        data_list (list of floats)
    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self):
        """
        Method to calculate mean of the datat set.
        :return:
            float: mean of the data set
        """
        avg = sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Method to calculate the standard deviation of the data set.
        :param
            sample (bool): whether the data represents a sample or population
        :return:
            float: standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean
        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)

        self.stdev = sigma
        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """
        Function to read data from a txt file
        :param
            file_name (string): name of a file to read from
        :param
            sample:
        :return:
            None
        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """
        Function to output histogram of the instance variable data using matplotlib pyplot lib
        :return:
        """
        plt.hist(self.data)
        plt.title('Histogram data')
        plt.xlabel('data')
        plt.ylabel('count')

    def pdf(self, x):
        """
        Probability density function calculator for gaussian distribution
        :param
            x (float): point for calculating the probability density function
        :return:
            float: probability density function
        """
        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mean) / self.stdev) ** 2)

    def plot_histogram_pdf(self, n_spaces=50):
        """
        Function to plot the normalized hist of the data and a plot of probability density
        function
        :param
            n_spaces (int): number of data points
        :return:
            list: x values for pdf plot
            list: y values for pdf plot
        """

        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)

        # Calculate the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # Calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # Make plot
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normalized Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y


