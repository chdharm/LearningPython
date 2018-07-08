import json

def pretty_print(data,current_indent=0,spaces=2):	
	items=[]	
	if type(data)==list:				
		items.append("[")
		items.append("\n")
		current_indent+=1
		items.append(" "*(current_indent*spaces))
		temp=[]
		
		for elem in data:
			temp.append(pretty_print(elem,current_indent,spaces))			
		
		delim=","+"\n"+(" "*(current_indent*spaces))
		current_indent-=1
		items.append(delim.join(temp))
		items.append("\n")
		items.append(" "*(current_indent*spaces))
		items.append("]")
		return "".join(items)
	elif type(data)==dict:		
		items.append("{")
		items.append("\n")
		current_indent+=1
		inner_items=[]
		for key,val in data.iteritems():
			temp=[]
			temp.append(" "*(current_indent*spaces))
			temp.append("\"")
			temp.append(str(key))
			temp.append("\"")
			temp.append(":")
			temp.append(" ")
			child=pretty_print(val,current_indent,spaces)
			#print child
			temp.append(child)
			inner_items.append("".join(temp))	
		current_indent-=1
		delim=","+"\n"+(" "*(current_indent*spaces))
		
		items.append(delim.join(inner_items))
		
		items.append("\n")
		items.append(" "*(current_indent*spaces))
		items.append("}")		
		return "".join(items)
	elif type(data)==str or type(data)==unicode:
		return "\""+str(data) + "\""
	elif type(data)==int or type(data)==float:
		return str(data)
	else:
		raise Exception("inval=id json value type")
	

#print pretty_print({"a":{"b":{"c":3}},"d":[1,2,"a","3","5"]})		
#print pretty_print({"a":1,"b":2,"c":3})		
#print pretty_print({"a":[1,2,3,4]})
#print pretty_print({1:'one',2:'two'})
print pretty_print([3434,'32r4',4378473873])
