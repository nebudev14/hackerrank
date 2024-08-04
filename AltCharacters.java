/* https://www.hackerrank.com/contests/mlh-fellowship-22-summer-pe-2/challenges/alternating-characters */

public class AltCharacters {
  public static int alternatingCharacters(String s) {
    int result = 0;
    
    for(int i = 1; i < s.length(); i++) {
      if(s.charAt(i) == s.charAt(i-1)) result++;
    }
    return result;
  }

  public static void main(String[] args) {
    System.out.println(alternatingCharacters("AAABBB"));
  }
}