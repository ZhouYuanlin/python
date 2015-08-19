from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize,1))-dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCout[voteIlabel] = classCount.get(voteIlabel,0) + 1
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1),reverse= True)
	return sortedClassCount[0][0]

def file2matrix(filename):
	fin = open(filename)
	arrayOLines = fin.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = zeros((numberOfLines, 3))
	index = 0
	classLabelVector = []
	for line in arrayOLines:
		listFormline = line.strip().split('\t')
		returnMat[index, : ] = listFormline[:3]
		classLabelVector.append(int(listFormline[-1]))
		index += 1
	return returnMat, classLabelVector

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDateSet = zeros(shape(dataSet))
	m = dataSet.shape(0)
	normDateSet = dataSet - tile(minVals, (m,1))
	normDateSet = normDateSet / (tile(ranges, (m,1)))
	return normDateSet, ranges, minVals




				
