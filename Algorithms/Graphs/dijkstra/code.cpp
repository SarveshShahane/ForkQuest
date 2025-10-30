#include <bits/stdc++.h>
using namespace std;

void dijkstra(int n, vector<vector<pair<int, int>>>& adj, int src) {
   
    


}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); 
    }

    int src;
    cin >> src;

    dijkstra(n, adj, src);

    return 0;
}
 