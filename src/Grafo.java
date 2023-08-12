package src;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

public class Grafo {
    public int[][] matriz;
    public ArrayList<LinkedList<Integer>> listas;
    public int n;

    public Grafo (String path) throws FileNotFoundException {
        _inicializar(path);
    }

    // 1
    private void _inicializar (String path) throws FileNotFoundException {
        Scanner scan = new Scanner(new File(path));
        this.n       = scan.nextInt();
        this.matriz  = new int[n][n];
        this.listas  = new ArrayList<LinkedList<Integer>>(n);
        
        int i, j, k;
        
        i = 0;
        while(scan.hasNextLine()) {
            listas.add(i, new LinkedList<Integer>());
            for (j = 0; j < n; j++) {
                k = scan.nextInt();
                matriz[i][j] = k;
                if (k != 0)
                listas.get(i).add(j+1);
            }
            i++;
        }
        scan.close();
    }

    //2
    public int dMax () {
        if (n == 0)
            return 0;

        int i, temp, max;

        max = listas.get(0).size();
        for (i = 1; i < n; i++) {
            temp = listas.get(i).size();
            max = temp > max ? temp : max;
        }

        return max;
    }

    public int dMin () {
        if (n == 0)
            return 0;
            
        int i, temp, min;

        min = listas.get(0).size();
        for (i = 1; i < n; i++) {
            temp = listas.get(i).size();
            min = temp < min ? temp : min;
        }

        return min;
    }

    // 3
    public int[] sequenciaGrau () {
        int[] graus = new int[n];
        int i, j, k;
        for (i = 0; i < n; i++) {
            j = i-1;
            k = listas.get(i).size();
            while (j >= 0 && graus[j] > k) {
                graus[j+1] = graus[j];
                j-=1;
            }
            graus[j+1] = k;
        }
        return graus;
    }

    // 4
    public int grau (int v) {
        if (v < 1 || v > n || listas.size() == 0)
            return 0;

        return listas.get(v-1).size();
    }

    public LinkedList<Integer> vAberta (int v) {
        if (v < 1 || v > n)
            return null;
        return listas.get(v-1);
    }

    public LinkedList<Integer> vFechada (int v) {
        if (v < 1 || v > n)
            return null;

        LinkedList<Integer> aux = listas.get(v-1);
        aux.add(v-1, v);

        return aux;
    }

    // 5
    public boolean ehAdjacente (int u, int v) {
        if (u < 1 || v < 1 || u > n || v > n)
            return false;
        
        return (matriz[u-1][v-1] == 1);
    }

    // 6
    public int ehRegular1 () {
        int i, v, k;
        
        v = listas.get(0).size();
        for (i = 1; i < n; i++) {
            k = listas.get(i).size();
            if (k != v)
                return -1;
        }
        return v;
    }

    public int ehRegular2 () {
        if (dMax() == dMin())
            return listas.get(0).size();
        
        return -1;
    }

    // 7
    public boolean completude () {
        Iterator<LinkedList<Integer>> it = listas.iterator();
        int k = (n*(n-1))/2;
        int count = 0;

        while (it.hasNext())
            count += it.next().size();
        
        return (count/2) == k;
    }

    // 8
    public LinkedList<Integer> verticesUniversais () {
        LinkedList<Integer> aux, out;
        Iterator<LinkedList<Integer>> it = listas.iterator();

        out = new LinkedList<Integer>();
        
        int i = 0;
        while (it.hasNext()) {
            aux = it.next();
            if (aux.size() == n-1)
                out.addLast(i+1);
            i++;
        }

        return out;
    }

    //9
    public LinkedList<Integer> verticesIsolados () {
        LinkedList<Integer> aux, out;
        Iterator<LinkedList<Integer>> it = listas.iterator();
        
        out = new LinkedList<Integer>();
        
        int i = 0;
        while (it.hasNext()) {
            aux = it.next();
            if (aux.size() == 0)
                out.addLast(i+1);
            i++;
        }
        return out;
    }
    

    // 10
    public boolean ehSub (int[] n, Aresta[] m) {
        if (n.length > this.n)
            return false;

        int i, a, b;
        for (i = 0; i < m.length; i++) {
            a = m[i].a;
            b = m[i].b;

            if (a > this.n || b > this.n)
                return false;
            if (a-1 < 0 || b-1 < 0)
                return false;
            if (matriz[a-1][b-1] == 0)
                return false;
        }

        return true;
    }

    //11
    public boolean ehPasseio (int[] n) {
        if (n.length <= 1)
            return true;
            
        int i, a, b;
        for (i = 0; i < n.length-1; i++) {
            a = n[i];
            b = n[i+1];

            if (a-1 < 0 || b-1 < 0)
                return false;

            if (matriz[a-1][b-1] != 1)
                return false;
        }

        return true;
    }

    // 12
    public boolean ehCaminho (int[] n) {  
        if (n.length <= 1)
            return true;

        int i, j, k;
        i = 0;

        while (i < n.length) {
            k = n[i];
            j = i+1;
            i = j;

            while (j < n.length)
                if (n[j++] == k)
                    return false;
        }

        return ehPasseio(n);
    }

    //13
    public boolean ehCiclo (int[] n) {
        if (n.length <= 1)
            return true;

        int i, j, k;
        i=0;
        while (i < n.length-1) {
            k = n[i];
            j = i+1;
            i = j;

            while (j < n.length)
                if (n[j++] == k)
                    return false;
        }
        return ehPasseio(n) && n[0] == n[n.length-1];
    }

    //14
    public boolean ehTrilha (int[] n) {

        return ehPasseio(n);
    }

    // AUXILIARES
    public String toStringMatriz() {
        String out = "";
        int i, j;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++)
                out += "%d ".formatted(matriz[i][j]);
            out += "\n";
        }
        return out;
    }

    public String toStringLista() {
        String out = "";
        int i;
        Iterator<Integer> it;
        for (i = 0; i < n; i++) {
            it = listas.get(i).listIterator();
            while(it.hasNext())
                out += "%d ".formatted(it.next());
            out += "\n";
        }
        return out;
    }
}