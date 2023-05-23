import java.util.ArrayList;
import java.util.List;

// 가비지 컬렉션으로도 메모리 누수가 발생될 때
/*
GC 인스턴스를 생성하고, addToMyList 메서드를 통해 list에 100만 개의 문자열을 
추가함
이때, list 변수는 인스턴스 변수로 선언되어 있기 때문에,  GC 인스턴스가 
소멸될 때까지 메모리에 계속 남아있다. 따라서, 가비지 컬렉션으로도 해당 메모리를 
해제할 수 없기 때문에, 메모리 누수가 발생한다.
 */
public class GC {
    private List<String> list = new ArrayList<>();
    
    public void addToMyList(String str) {
        list.add(str);        
    }
    
    public static void main(String[] args) {
        GC gc = new GC();
        for (int i = 0; i < 1000000; i++) {
            gc.addToMyList("string" + i);
        }
    }
    
}