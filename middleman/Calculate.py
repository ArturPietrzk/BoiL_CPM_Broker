import copy
import math


def isTableFilled(tab):
    for i in range(0, len(tab) - 1):
        for j in range(0, len(tab[0]) - 1):
            if tab[i][j] == False:
                return False
    return True


class Calculations:
    def __init__(self):
        self.transportTable = None
        self.optimizationTable = None
        self.alpha = None
        self.beta = None
        self.tempAlpha = None
        self.tempBeta = None

    # Zmiana wartosci w tablicach poczatkowych na NaN
    def setup(self, provider, recipient, profits):

        # Add imaginary recipient and provider
        currentStateProvider: [int] = copy.deepcopy(provider)
        currentStateRecipient: [int] = copy.deepcopy(recipient)
        self.transportTable = [[0 for j in range(len(recipient) + 1)] for i in range(len(provider) + 1)]
        isFilled = [[False for j in range(len(recipient) + 1)] for i in range(len(provider) + 1)]

        imaginaryProvider: int = 0
        imaginaryRecipient: int = 0
        for i in range(0, len(recipient)):
            imaginaryProvider += recipient[i]
        for i in range(0, len(provider)):
            imaginaryRecipient += provider[i]

        currentStateProvider.append(imaginaryProvider)
        currentStateRecipient.append(imaginaryRecipient)

        maxValue: float = 0.0
        maxValueCoordinates: [int] = [0] * 2
        wasMaxValueAssigned: bool

        while not isTableFilled(isFilled):
            wasMaxValueAssigned = False
            for i in range(0, len(profits)):
                for j in range(0, len(profits[0])):
                    if not (isFilled[i][j]):
                        if not wasMaxValueAssigned:
                            maxValue = profits[i][j]
                            maxValueCoordinates[0] = i
                            maxValueCoordinates[1] = j
                            wasMaxValueAssigned = True

                        elif profits[i][j] > maxValue:
                            maxValue = profits[i][j]
                            maxValueCoordinates[0] = i
                            maxValueCoordinates[i] = j

            if currentStateProvider[maxValueCoordinates[0]] >= currentStateRecipient[maxValueCoordinates[1]]:
                self.transportTable[maxValueCoordinates[0]][maxValueCoordinates[1]] = currentStateRecipient[maxValueCoordinates[1]]
                currentStateProvider[maxValueCoordinates[0]] -= currentStateRecipient[maxValueCoordinates[1]]
                currentStateRecipient[maxValueCoordinates[1]] = 0
                for i in range(0, len(isFilled)):
                    isFilled[i][maxValueCoordinates[1]] = True

            else:
                self.transportTable[maxValueCoordinates[0]][maxValueCoordinates[1]] = currentStateProvider[
                    maxValueCoordinates[0]]
                currentStateRecipient[maxValueCoordinates[1]] -= currentStateProvider[maxValueCoordinates[0]]
                currentStateProvider[maxValueCoordinates[0]] = 0
                for i in range(0, len(isFilled[0])):
                    isFilled[maxValueCoordinates[0]][i] = True

        for i in range(0, len(self.transportTable[0]) - 1):
            if not isFilled[len(provider)][i]:
                self.transportTable[len(provider)][i] = currentStateRecipient[i]
                currentStateProvider[len(provider)] -= currentStateRecipient[i]
                currentStateRecipient[i] = 0
                isFilled[len(provider)][i] = True

        for i in range(0, len(self.transportTable)):
            if not isFilled[i][len(recipient)]:
                self.transportTable[i][len(recipient)] = currentStateProvider[i]
                currentStateRecipient[len(recipient)] -= currentStateProvider[i]
                currentStateProvider[i] = 0
                isFilled[i][len(recipient)] = True

    # Powinno działać
    def findAlphaBeta(self, alpha: [float], beta: [float], profits):
        isValue: bool = True

        self.tempAlpha = alpha[:]
        self.tempBeta = beta[:]
        for i in range(0, len(alpha)):
            if math.isnan(alpha[i]):
                isValue = False

        for i in range(0, len(beta)):
            if math.isnan(beta[i]):
                isValue = False
        if isValue:
            return

        for i in range(0, len(alpha)):
            for j in range(0, len(beta)):
                if self.transportTable[i][j] > 0:
                    if math.isnan(beta[j]) and (not math.isnan(alpha[i])):
                        if (j >= len(profits[0])) or (i >= len(profits)):
                            beta[j] = 0.0 - alpha[i]
                        else:
                            beta[j] = profits[i][j] - alpha[i]
                    elif (not math.isnan(beta[j])) and (math.isnan(alpha[i])):
                        if i >= len(profits) or j >= len(profits[0]):
                            alpha[i] = 0.0 - beta[j]
                        else:
                            alpha[i] = profits[i][j] - beta[j]

        if (self.tempAlpha == alpha) and (self.tempBeta == beta):
            for i in range(0, len(alpha)):
                if math.isnan(alpha[i]):
                    alpha[i] = 0
                    break

        self.findAlphaBeta(alpha, beta, profits)

    # Powinno działać
    def constructOptTable(self, alpha: [float], beta: [float], profits):
        for i in range(0, len(self.transportTable)):
            for j in range(0, len(self.transportTable[0])):
                if self.transportTable[i][j] != 0:
                    self.optimizationTable[i][j] = float('NaN')
                else:
                    self.optimizationTable[i][j] = self.transportTable[i][j] - alpha[i] - beta[j]

    # Powinno działać
    def isOptimal(self):
        for i in range(0, len(self.optimizationTable)):
            for j in range(0, len(self.optimizationTable[0])):
                if self.optimizationTable[i][j] > 0:
                    return False
        return True

    def applyCycle(self):
        maxVal: float = 0.0
        optimalPathCoordinates = [[0 for j in range(2)] for i in range(4)]

        for i in range(0, len(self.optimizationTable)):
            for j in range(0, len(self.optimizationTable[0])):
                if (not math.isnan(self.optimizationTable[i][j])) and (self.optimizationTable[i][j] > maxVal):
                    maxVal = self.optimizationTable[i][j]
                    optimalPathCoordinates[0][0] = i
                    optimalPathCoordinates[0][1] = j

        wasPathAssigned: bool = False
        optimalPathCoordinates[1][0] = optimalPathCoordinates[0][0]
        optimalPathCoordinates[3][1] = optimalPathCoordinates[0][1]

        for i in range(0, len(self.optimizationTable[0])):
            if i != optimalPathCoordinates[0][1]:
                if math.isnan((self.optimizationTable[optimalPathCoordinates[0][0]][i])):
                    for j in range(0, len(self.optimizationTable)):
                        if j != optimalPathCoordinates[0][0]:
                            if (math.isnan(self.optimizationTable[j][i])) and math.isnan(
                                    self.optimizationTable[j][optimalPathCoordinates[0][1]]):
                                optimalPathCoordinates[1][1] = i
                                optimalPathCoordinates[2][0] = j
                                optimalPathCoordinates[2][1] = i
                                optimalPathCoordinates[3][0] = j
                                wasPathAssigned = True
                                break

            if (wasPathAssigned):
                break

        changeValue: int = min(self.transportTable[optimalPathCoordinates[1][0]][optimalPathCoordinates[1][1]],
                               self.transportTable[optimalPathCoordinates[3][0]][optimalPathCoordinates[3][1]])
        self.transportTable[optimalPathCoordinates[0][0]][optimalPathCoordinates[0][1]] += changeValue
        self.transportTable[optimalPathCoordinates[1][0]][optimalPathCoordinates[1][1]] -= changeValue
        self.transportTable[optimalPathCoordinates[2][0]][optimalPathCoordinates[2][1]] += changeValue
        self.transportTable[optimalPathCoordinates[3][0]][optimalPathCoordinates[3][1]] -= changeValue

    def compute(self, provider: [int], recipient: [int], profits):
        self.setup(provider, recipient, profits)

        while True:
            self.alpha: [float] = [float('Nan')] * (len(profits) + 1)
            self.beta: [float] = [float('Nan')] * (len(profits[0]) + 1)

            self.findAlphaBeta(self.alpha, self.beta, profits)

            self.optimizationTable = [[0 for j in range(len(recipient) + 1)] for i in range(len(provider) + 1)]
            self.constructOptTable(self.alpha, self.beta, profits)

            if self.isOptimal():
                break

            self.applyCycle()

        return self.transportTable
