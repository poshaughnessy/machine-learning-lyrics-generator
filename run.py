from textgenrnn import textgenrnn

textgen = textgenrnn()

textgen.train_from_file('pavement-lyrics.txt', num_epochs=5)

textgen.generate()
