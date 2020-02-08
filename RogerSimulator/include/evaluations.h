#define PONG 0
#define MAX_TIME 10.0
#define MAX_POSSESSION_TIME 1.0
#define MAX_SCORE 11
#define R_GOAL 0.35

typedef struct _pong_evaluator {

  double possession_time_1;
  double possession_time_2;

  double continuous_possession_time_1;
  double continuous_possession_time_2;

  int goal_1;
  int goal_2;

} PongEval;
