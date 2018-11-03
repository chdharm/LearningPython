import re
ip="""{"abc":"def","af":"","hh":{"a":1},"d":"{","hh":"["}
"""
ip=ip[:-1]

def parse(ip):

	match= re.match(r'\"(.*)\"',ip)
	if match:
		return match.groups()[0]
	else:
		int_val=None

		try:
		 	int_val=int(ip)
		except Exception as e:
		 	pass
		else:
		 	return int_val
		if int_val is None:
			match= re.match(r'\{(.*)\}',ip)
			if match:
				child_val = match.groups()[0]
				child_val+=","
				all_pairs = re.findall(r'\"(\w+?)\"\:(.*?),',child_val)
				d={}
				for key,val in all_pairs:
					d[key]=parse(val)
				return d
			else:
				print ip
				match= re.match(r'\[(.*)\]',ip)
				print "lmatch",match
				if match:
					child_val = match.groups()[0]
					child_val+=","
					all_items=re.findall(r'(.+?),',child_val)
					l=[]
					l=[item for item in all_items ]
					return l
	raise Exception("invalid json")
print parse(ip)