package src;

import java.util.LinkedList;

public class Teste {

    public static void q1(Grafo g) {
        System.out.println("Matriz:\n%s".formatted(g.toStringMatriz()));
        System.out.println("Lista: \n%s".formatted(g.toStringLista()));
    }

    public static void q2(Grafo g) {
        System.out.println("d(G) = %d".formatted(g.dMin()));
        System.out.println("D(G) = %d".formatted(g.dMax()));
    }

    public static void q3(Grafo g) {
        System.out.print("sequencia de grau: ");
        _printv(g.sequenciaGrau());
    }

    public static void q4(Grafo g, int u) {
        System.out.println("grau de V(%d) = %d".formatted(u, g.grau(u)));
        System.out.println("vizinhanca aberta de %d: ".formatted(u) + g.vAberta(u));
        System.out.println("vizinhanca fechada de %d: ".formatted(u) + g.vFechada(u));
    }

    public static void q5(Grafo g, int u, int v) {
        System.out.println(g.ehAdjacente(u, v) ? "(%d, %d) sao adj.".formatted(u, v) : "(%d, %d) NAO sao adj.".formatted(u, v));
    }

    public static void q6(Grafo g) {
        int o = g.ehRegular1();
        if (o < 0)
            System.out.println("G NAO eh regular");
        else
            System.out.println("G eh %d-regular".formatted(o));
    }

    public static void q7(Grafo g) {
        System.out.println("G %seh completo".formatted(g.ehCompleto() ? ""  : "NAO "));
    }

    public static void q8(Grafo g) {
        LinkedList<Integer> n = g.verticesUniversais();
        System.out.println(
            "vertices universais: %s"
            .formatted(n.size() == 0 ? "NAO ha vertice universal" : n.toString()));
    }

    public static void q9(Grafo g) {
        LinkedList<Integer> n = g.verticesIsolados();
        System.out.println(
            "vertices isolados: %s"
            .formatted(n.size() == 0 ? "NAO ha vertice isolado" : n.toString()));
    }

    public static void q10 (Grafo g, int[] n, int[] m) {
        _printvDupla(m);
        System.out.print(" %seh subgrafo\n".formatted((g.ehSub(n, m) ? "" : "NAO")));
    }

    public static void q11 (Grafo g, int[] n) {
        _printv(n);
        System.out.print(" %seh passeio\n".formatted((g.ehPasseio(n) ? "" : "NAO ")));
    }

    public static void q12 (Grafo g, int[] n) {
        _printv(n);
        System.out.print(" %seh caminho\n".formatted((g.ehCaminho(n) ? "" : "NAO ")));
    }

    public static void q13 (Grafo g, int[] n) {
        _printv(n);
        System.out.print(" %seh ciclo\n".formatted((g.ehCiclo(n) ? "" : "NAO ")));
    }

    public static void q14 (Grafo g) {
    
    }

    public static void q15 (Grafo g, int[] n) {
        _printv(n);
        System.out.print(" %seh clique\n".formatted((g.ehClique(n) ? "" : "NAO ")));
    }

    public static void q17 (Grafo g) {
        Grafo gl = g.complemento(g);
        System.out.println("Complemento de G");
        System.out.println(g.toStringMatriz());
        System.out.println(gl.toStringMatriz());
        System.out.println(g.toStringLista());
        System.out.println(gl.toStringLista());
    }

    public static void q18 (Grafo g, int [] n) {
        _printv(n);
        System.out.print(" %seh conjunto independente ".formatted(g.ehIndependente(n)? "" : "NAO "));
    }

    private static void _printv(int[] v) {
        System.out.print("{ ");
        for (int i : v)
            System.out.print("%d ".formatted(i));
        System.out.print("}");
    }

    private static void _printvDupla (int[] v) {
        System.out.print("{ ");
        for (int i = 0; i < v.length; i++) 
            System.out.print("(%d,%d) ".formatted(v[i], v[++i]));
        System.out.print("}");
    }
}
