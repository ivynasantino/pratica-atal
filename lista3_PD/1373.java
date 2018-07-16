import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int k = 1;
        while (k != 0){
            k = in.nextInt();
            if(k == 0) break;
            in.nextLine();
            String palavra1 = in.nextLine();
            String palavra2 = in.nextLine();
            System.out.println(dnaSequence(palavra1, palavra2, k));
        }
    }
	public static int dnaSequence(String palavra1, String palavra2, int k) {
        int l1 = palavra1.length();
        int l2 = palavra2.length();
        int[][] matriz = new int[l1 + 1][l2 + 1];
        for (int i = 1; i <= l1; i++) {
            for (int j = 1; j <= l2; j++) {
                int n = 0;
                matriz[i][j] = Math.max(matriz[i - 1][j], matriz[i][j - 1]);
                while (i - 1 - n >= 0 && j - 1 - n >= 0 && palavra1.charAt(i - 1 - n) == palavra2.charAt(j - 1 - n)) {
                    n++;
                }
                if (n >= k) {
                    for (int p = k; p <= n; p++) {
                        matriz[i][j] = Math.max(matriz[i][j], matriz[i - p][j - p] + p);
                    }
                }
            }
        }

        return matriz[l1][l2];
    }
}
