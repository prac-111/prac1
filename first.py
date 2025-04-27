from mrjob.job import MRJob

class MRWordCount(MRJob):
    
    def mapper(self, _, line):
        for word in line.split():
            yield (word.lower(), 1)
    
    def reducer(self, word, counts):
        yield (word, sum(counts))

MRWordCount.run()