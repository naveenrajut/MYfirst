import networkx as nx
import matplotlib.pyplot as plt
import yaml

g=nx.OrderedGraph()
node_Colours=[]
graph=[]

def yaml_load_file():						# THIS FUNCTION IS USED TO LOAD THE YAML FILE FROM UNIVERSITY.YAML
	with open('university.yaml','r') as f:  # IT OPENS THE YAML FILE IN READ MODE AS F(FILE)
		return (yaml.load(f))				# HERE IT LOADS THE YAML FILE IN DICTIONARY FORMAT
	

def draw_graph(data):						# THIS FUNCTION IS TO CREATE NODE'S AND FORM EDGES BETWEEN THE NODES
	for k,v in data.items():
		colourNodes(len(v.keys()))			# IT CALLS COLOURNODES FUNCTION TO COLOUR THE NODE, THAT HOLD IN KEYS OF VALUES 
		for i in v.keys():
			g.add_edge(k,i)					# CREATS THE EDGES BETWEEN TWO NODES
			if type(v[i]) is not str:
				colourNodes(len(v[i]))
				draw_graph(v)
			elif type(v[i]) is str:
				a=str(v[i]).split(',')		# SPLITS THE VALUE OF STUDENTS AND PROFESSORS WITH THE INTERVAL OF COMMA(,)
				for j in a:
					g.add_edge(i,j)
					graph.append(j)			# APPEND THE VALUE OF INDIVIDUAL STUDENTS AND PROFFESORS FOR THE CREATION OF EDGES BETWEEN THEM
					colourNodes(len(a))
				colourNodes(len(a))
					

def addEdges():								# THIS FUNCTION IS TO CREATE THE EDGES BETWEEN STUDENTS TO PROFESSORS, PROFESSORS TO PROFESSORS, STUDENTS TO STUDENTS
	for i in range(len(graph)):
		for j in range(i+1,len(graph)):
			g.add_edge(graph[i],graph[j])


def colourNodes(length):					# THIS FUNCTION IS TO COLOUR THE NODES BASED ON THEIR FEILD OR ENTITIES
	if length == 2:							# THIS COMPARES NUMBER OF GROUPS UNDER EACH DEPARTMENT(EACH DEPARTMENT HAS TWO GROUPS STUDENTS AND PROFESSORS)
		node_Colours.append('green')
	elif length == 6:						# COMPARES NUMBER OF PROFESSORS 
		node_Colours.append('red')
	elif length == 20:						# COMPARES NUMBER OF STUDENTS
		node_Colours.append('blue')

def makeLegend():							# THIS FUNCTION IS USED TO CREATE A INFORMATION BOX 
	fig=plt.figure('SOCIAL MAP OF THE UNIVERSITY')# TITLE OF OUR WINDOW
	ax=fig.add_subplot(1,1,1)
	d={'departments':'green','professors':'red','students':'blue'}
	for i in d.keys():
		ax.plot(0,0,color=d[i],label=i)
	plt.legend(loc='upper right')			# PLACING THE INFORMATION BOX AT THE UPPER RIGHT CORNER
	

def main():									# THIS MAIN FUNCTION IS JUST TO CALL ALL FUCTION
	data=yaml_load_file()
	graph=draw_graph(data)
	addEdges()
	colourNodes(data)
	makeLegend()
	pos=nx.spring_layout(g)
	nx.draw(g,pos=pos,node_color=node_Colours,with_labels=False)
	plt.show()								# THIS SHOWS THE CREATED GRAPH IIN THE NEW WINDOW
	

if __name__=="__main__":
	main()
