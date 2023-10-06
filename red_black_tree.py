import algviz
class rb_node:
    def __init__(self, value=None, left= None, right= None, color=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
    
    def rb_insert(self, new_node):
        parent_node = None
        search_node = self
        while search_node != None:
            parent_node = search_node
            if new_node.value < search_node.value:
                if search_node.left.value == nil_node:
                    new_node.parent = parent_node
                    search_node.left = new_node
                search_node = search_node.left
            else:
                if search_node.right.value == nil_node:
                    new_node.parent = parent_node
                    search_node.right = new_node
                search_node = search_node.right
        if parent_node == nil_node:
            self = new_node
        elif new_node.value < parent_node.value:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        new_node.left = nil_node
        new_node.right = nil_node
        new_node.color = "red"
        self.rb_insert_fixup(new_node)

    def rb_insert_fixup(self, new_node):
        while new_node.parent.color == "red":
            if new_node.parent == new_node.parent.parent.left:
                parent_node = new_node.parent.parent.right
                if parent_node.color == "red":
                    new_node.parent.color = "black"
                    parent_node.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                elif new_node == new_node.parent.right:
                    new_node = new_node.parent
                    self.left_rotation()
                else:
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.right_rotation()
            else:
                parent_node = new_node.parent.parent.left
                if parent_node.color == "red":
                    new_node.parent.color = "black"
                    parent_node.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                elif new_node == new_node.parent.left:
                    new_node = new_node.parent
                    self.right_rotation()
                else:
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.left_rotation()
        self.color = "black"
                

                    
    def left_rotation(self, pivot_node):
        pivot_successor = pivot_node.right
        pivot_node.right = pivot_successor.left
        if pivot_successor.left != nil_node:
            pivot_successor.left.parent = pivot_node
        elif pivot_node == pivot_node.parent.left:
            pivot_node.parent.left = pivot_successor
        else:
            pivot_node.parent.right = pivot_successor
        pivot_successor.left = pivot_node
        pivot_node.parent = pivot_successor

    def right_rotation(self, pivot_node):
        nil_node = self.__init__()
        pivot_successor = pivot_node.left
        pivot_node.left = pivot_successor.right
        if pivot_successor.right != nil_node:
            pivot_successor.right.parent = pivot_node
        elif pivot_node == pivot_node.parent.right:
            pivot_node.parent.right = pivot_successor
        else:
            pivot_node.parent.left = pivot_successor
        pivot_successor.right = pivot_node
        pivot_node.parent = pivot_successor

    def rb_transplant(self, u, v):
        if u.parent == nil_node:
            self = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def rb_delete(self, deletion_node):
        del_node = deletion_node
        del_node_color = deletion_node.color
        child_node = None
        if deletion_node.left == nil_node:
            child_node = deletion_node.right
            self.rb_transplant(deletion_node, deletion_node.left)
        elif deletion_node.right == nil_node:
            child_node = deletion_node.left
            self.rb_transplant(deletion_node, deletion_node.right)
        else:
            del_node = self.tree_minimum()
            del_node_color = del_node.color
            child_node = del_node.right
            if (del_node.parent == deletion_node):
                child_node.parent = del_node
            else:
                self.rb_transplant(del_node, del_node.right)
                del_node.right = deletion_node.right
                del_node.right.parent = del_node
            self.rb_transplant(deletion_node, del_node)
            del_node.left = deletion_node.left
            del_node.left.parent = del_node
            del_node.color = deletion_node.color
        if del_node_color == "black":
            self.rb_delete_fixup(child_node)
    def rb_delete_fixup(self, child_node):
        while child_node != self and child_node.color == "black":
            if child_node == child_node.parent.left:
                w = child_node.parent.right
                if w.color == "red":
                    w.color = "black"
                    child_node.parent.color = "red"
                    self.left_rotation(child_node.parent)
                    w = child_node.parent.right
                elif w.right.color == "black":
                    w.left.color = "black"
                    w.color = "red"
                    self.right_rotation(w)
                    w = child_node.parent.right
                w.color = child_node.parent.color
                child_node.parent.color = "black"
                w.right.color = "black"
                self.left_rotation(child_node.parent)
                child_node = self
            else:
                w = child_node.parent.left
                if w.color == "red":
                    w.color = "black"
                    child_node.parent.color = "red"
                    self.right_rotation(child_node.parent)
                    w = child_node.parent.left
                elif w.left.color == "black":
                    w.right.color = "black"
                    w.color = "red"
                    self.left_rotation(w)
                    w = child_node.parent.left
                w.color = child_node.parent.color
                child_node.parent.color = "black"
                w.left.color = "black"
                self.right_rotation(child_node.parent)
                child_node = self
        child_node.color = "black"

    def tree_maximum(self):
        search_node = self
        while search_node.right != None:
            search_node = search_node.right
        return search_node

    def tree_minimum(self):
        search_node = self
        while search_node.left != None:
            search_node = search_node.left
        return search_node
        
        
global nil_node
nil_node = rb_node()