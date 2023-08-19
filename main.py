import eval.evaluate
import generate
if __name__ == '__main__':
    a = generate.buildTree(10).toString()
    print(a)
    b = eval.evaluate.evaluate(a)
    print(b)

