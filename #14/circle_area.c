#include <math.h>
#include <stdio.h>

#include <time.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/random.h>

static
void new_seed() {
    unsigned seed;
    if (getrandom(&seed, sizeof(seed), GRND_RANDOM) < 0) {
        srandom(seed);
    } else {
        srandom(time(NULL));
    }
}

static inline
/* random double between 0 and 1 */
double random_double(void) {
    static bool first_run = true;

    if (first_run) {
        new_seed();
        first_run = false;
    }

    long rand_int = random();
    return ((double) rand_int) / ((double) RAND_MAX);
}


double calc_pi(int points) {
    double const radius = 1.0;
    double const radius_sq = radius * radius;

    int inside = 0;
    for (int i = 0; i < points; i++) {
        double const x = random_double();
        double const y = random_double();

        double const dist_sq = x*x + y*y;

        if (dist_sq <= radius_sq) {
            inside++;
        }
    }

    double const area_factor = ((double) inside) / ((double) points);
    double const square_area = 1.0 * 1.0;

    double const circle_area = 4 * area_factor * square_area;

    double pi = circle_area / radius_sq;

    return pi;
}

int main(int argc, char const *argv[]) {
    for (int i = 1; i < argc; i++) {
        int points = atoi(argv[i]);

        if (points > 0) {
            double pi = calc_pi(points);

            printf("With %d points, Monte Carlo's give us: pi = %lf.\n",
                points, pi
            );
        }
    }

    return 0;
}
