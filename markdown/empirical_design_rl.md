# Empirical Design in Reinforcement Learning

A love letter to
[Empirical Design in Reinforcement Learning](arxiv.org/pdf/2304.01315)
by Andrew Patterson, Samuel Neumann, Martha White, Adam White / 
JMLR 25 (2024) 1-63 / 
(from this [Bluesky post](https://bsky.app/profile/brohrer.bsky.social/post/3lbmmmelles2t))

These aren’t the heroes we deserve, but they are the heroes we need.

I mean, look at this opening paragraph. This is written to be read and understood, not to impress and overwhelm. Not for the handful of reinforcement learning researchers in the world, but for the slightly larger handful of people trying to make it work on their machine.

The paper is refreshingly concrete, fully loaded with examples, case studies, recommendations, and pitfalls. It's a map to the landmines in reinforcement learning. It's what I would have gifted my younger self.

![Reinforcement Learning, an Empirical Science
Running a good experiment in reinforcement learning is difficult. There are many decisions
to be made: How long should you run your agent? Should you count the number of episodes
or number of steps? Should performance be measured online or offline with test trials?
How should you measure and aggregate performance? Do we use rules of thumb to set
hyperparameters or some systematic search? What are the right baseline algorithms to
compare against? Which environments should you use? What does good learning even look
like in a given environment? The answer to each question can greatly impact the credibility
and utility of the result, ranging from insightful to down-right misleading](
https://brandonrohrer.com/images/empirical_rl/img_a.png
"Opening paragraph from the paper")

![Alt text](https://assets.digitalocean.com/articles/alligator/boo.svg "a title")

It's easy to lie to your readers in any ML work, but in reinforcement learning it's also easy to lie to yourself. The authors shine a bright light on all these sneaky backchannels. Designer's curse. Untuned baselines. Hypothesis After Results Known (HARK). Cherrypicking of all sorts.

And for the love of the great Flying Spaghetti Monster DO NOT TUNE ON YOUR SEED. Just don't.

As an unexpected treat the authors have genuinely grown-up conversations with us about statistics. Reinforcement learning runs are so computationally intense and then add in hyperparameter sweeps, it's easy to see how representing distributions and confidence intervals falls by the wayside.
No more.


But the ride doesn't stop there. The authors take an ax to the root of the tree of ML leaderboard-based publishing. They make a strong case that reinforcement learning comparisons are all but infeasible to do in a meaningful way.

This low key refutes the entire ML conference industrial complex.
The authors even take it a step further. If you can always choose environments in which your algorithm excels, then the interesting question becomes *which* conditions and *why*. 
Each RL algorithm is a special and unique snowflake. What if the real science is the quirks we discovered along the way?

As an absolute tour de force, the authors attempt what has so far only been dreamed of - reproducing results from another paper. They prove that it's not a path for the faint of heart, but they get there, and in style.

You like lists? The authors finish with a list of common errors in reinforcement learning experiments.

1. Averaging over 3 or 5 runs
2. Reusing code from another source (including hyperparameters) as is
3. Untuned agents in ablations
4. Not controlling seeds
5. Discarding or replacing runs
6. Cutting off episodes early
7. Treating episode cutoffs as termination
8. Randomizing start states
9. HARK’ing (hypothesis after results known)
10. Environment overfitting
11. Overly complex algorithms
12. Choosing gamma incorrectly
13. Reporting offline performance while making conclusions about online performance
14. Invalid errorbars or shaded regions
15. Using random problems
16. Not reporting implementation details
17. Not comparing against stupid baselines
18. Running inefficient code
19. Attempting to run an experiment beyond your computational budget
20. Gatekeeping with benchmark problems
 
and they note that this list will be appended to in an accompanying online blog post.

The only thing the paper lacked IMO was it should have ended with *mic drop*


