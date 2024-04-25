class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children = [] 
        self.parent = None 
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        

def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Android"))
    cellphone.add_child(TreeNode("Nokia"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()

    # test that the add_child method worked
    print("=" * 40)
    print("Root Children")
    for child in root.children:
        print(child.data)

    print(f"")