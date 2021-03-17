def findPath(root, path, k):
    if root is None:
        return False
    path.append(root.key)
    if root.key == k:
        return True
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False

def findUniqueJobs(root, trees_elements):

    path = []
    for ele in trees_elements:
        current_path = []
        if not findPath(root, current_path, n1):
            return -1
        path.extends(current_path)
        current_path = []

    return list(set(path)) #Remove the jobs which were asked



