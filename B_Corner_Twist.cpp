#include <bits/stdc++.h>
using namespace std;

#define Faster ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr)
#define endl '\n'

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> a(n, vector<int>(m));
    vector<vector<int>> b(n, vector<int>(m));

    // Read grid a
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    // Read grid b
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> b[i][j];
        }
    }

    // Check if it's possible to convert a to b
    bool possible = true;
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < m - 1; ++j) {
            int dr = (b[i][j] - a[i][j] + 3) % 3;
            // Effect on the subrectangle (i, j) to (i+1, j+1)
            for (int di = 0; di <= 1; ++di) {
                for (int dj = 0; dj <= 1; ++dj) {
                    int ni = i + di;
                    int nj = j + dj;
                    a[ni][nj] = (a[ni][nj] + dr) % 3;
                }
            }
        }
    }

    // Check if a can be converted to b
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] != b[i][j]) {
                possible = false;
                break;
            }
        }
        if (!possible) break;
    }

    if (possible) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

int main() {
    Faster;
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}
