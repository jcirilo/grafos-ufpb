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

    public Grafo (int n) {
        this.n = n;
        this.matriz = new int[n][n];
        this.listas = new ArrayList<LinkedList<Integer>>(n);
        for (int i = 0; i < n; i++)
            listas.add(i, new LinkedList<Integer>());
    }

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

        for (i = 0; i < n; i++) {
            listas.add(i, new LinkedList<Integer>());
            for (j = 0; j < n; j++) {
                k = scan.nextInt();
                matriz[i][j] = k;
                if (k != 0) 
                    listas.get(i).add(j+1);
            }
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
    public int grau (int n) {
        if (n < 1 || n > this.n || listas.size() == 0)
            return 0;

        return listas.get(n-1).size();
    }

    public LinkedList<Integer> vAberta (int n) {
        if (n < 1 || n > this.n) 
            return null;
        
        return listas.get(n-1);
    }

    public LinkedList<Integer> vFechada (int n) {
        if (n < 1 || n > this.n)
            return null;

        LinkedList<Integer> aux = listas.get(n-1);
        aux.add(n-1, n);

        return aux;
    }

    // 5
    public boolean ehAdjacente (int a, int b) {
        if (a < 1 || b < 1 || a > n || b > n)
            return false;
        
        return (matriz[a-1][b-1] == 1);
    }

    // 6
    public int ehRegular1 () {
        int i, u, v;
        
        u = listas.get(0).size();
        for (i = 1; i < n; i++) {
            v = listas.get(i).size();
            if (v != u)
                return -1;
        }

        return u;
    }

    public int ehRegular2 () {
        if (dMax() == dMin())
            return listas.get(0).size();
        
        return -1;
    }

    // 7
    public boolean ehCompleto () {
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
    public boolean ehSub (int[] n, int[] m) {
        if (n.length > this.n)
            return false;
        
        for (int v : n)
            if (v > this.n)
                return false;

        for (int i = 0; i < n.length-1; i++)
            if (!ehAdjacente(n[i], n[++i]))
                return false;
        
        return true;
    }

    //11
    public boolean ehPasseio (int[] n) {            
        for (int i = 0; i < n.length-1; i++)
            if (!ehAdjacente(n[i], n[i+1]))
                return false;

        return true;
    }

    // 12
    public boolean ehCaminho (int[] n) { 
        if (n[0] == n[n.length-1])
            return false;

        if (!ehPasseio(n))
            return false;
        
        int i, j, k;
        i = 1;
        while (i < n.length-2) {
            j = i+1;
            k = n[i];
            i = j;
            while (j < n.length-1)
                if (k == n[j++])
                    return false;
        }

        return true;
    }

    //13
    public boolean ehCiclo (int[] n) {
        if (n[0] != n[n.length-1])
            return false;

        if (!ehPasseio(n))
            return false;

        int i, j, k;
        
        i = 1;
        while (i < n.length-2) {
            j = i+1;
            k = n[i];
            i = j;
            while (j < n.length-1)
                if (k == n[j++])
                    return false;
        }

        return true;
    }

    //14
    public boolean ehTrilha (int[] n) {
        if (!ehPasseio(n))
            return false;

        return true;
    }

    // 15
    public boolean ehClique (int[] n) {
        int i, j, a, b;
        i = 0;
        while (i < n.length-1 ) {
            a = n[i];
            j = i+1;
            i = j;
            while (j < n.length) {
                b = n[j];
                if (!ehAdjacente(a, b))
                    return false;
                j++;
            }
        }
        return true;
    }

    // 16
    public boolean ehCliqueMaximal (int[] n) {
        //int i, j, k;

        return true;
    }

    //17
    public Grafo complemento (Grafo g) {
        Grafo aux = new Grafo(g.n);

        for (int i = 0; i < g.n; i++) {
            for (int j = 0; j < g.n; j++) {
                aux.matriz[i][j] = (1 - g.matriz[i][j]);
                if(aux.matriz[i][j] == 1)
                    aux.listas.get(i).add(j+1);
            }
        }    
        return aux;
    }

    //18
    public boolean ehIndependente (int[] n) {
        Grafo gInverso = complemento(this);
        return gInverso.ehClique(n);
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