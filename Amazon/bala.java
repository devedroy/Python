import java.util.ArrayList;

class Result {
    ComponentNode node;
    double sum;
    int size;
    public Result(ComponentNode node, double sum, int size) {
        this.node = node;
        this.sum = sum;
        this.size = size;
    }
}
public static class ComponentNode {
    int value;
    ArrayList<ComponentNode> components;

    public ComponentNode(int value) {
        this.value = value;
        components = new ArrayList<>();
    }
    public ComponentNode() {
        components = new ArrayList<>();
    }
}
public ComponentNode getFastestComponent (ComponentNode rootComponent) {
    if(rootComponent == null) {
        return null;
    }
    helper(rootComponent);
    return res.node;
}
private Result res = null;

public Result helper(ComponentNode root) {
    if(root == null) {
        return new Result(null, 0, 0);
    }
    if(root.components.size() == 0) {
        return new Result(root, root.value, 1);
    }
    Result left = helper(root.components.get(0));
    Result right = helper(root.components.get(1));
    if(left.sum + right.sum > root.value) {
        if(left.size > right.size) {
            res = new Result(left.node, left.sum, left.size);
        } else {
            res = new Result(right.node, right.sum, right.size);
        }
    } else {
        res = new Result(root, root.value, left.size + right.size);
    }
    return res;
}