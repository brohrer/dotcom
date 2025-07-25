# Build with AI or traditional ML?

### Summary

Shoppi, a small company with a shopping list app, is building
a list completion feature.

A **large language model** provides

1. Simple architecture
2. Versatility beyond training data

A **recommender system** provides

1. Item discovery
2. High relevance

A **rule-based approach** provides

1. Low computation cost
2. Low latency
3. Transparency (explainability and debuggability)

The Shoppi team opted for a rule-based solution as a first step,
instead of an LLM or a recommender system,
because it suits their limited resources and aligns with their product strategy.
They plan to transition to a recommender system in 18 months,
as the engineering team and user base grows and allows them
to take advantage of their scale.

----------

## Scenario

Choosing whether to power an intelligent feature with a traditional
recommender system, hard-coded rules, or an LLM is a game of
give and take between several highly desirable charactertistics, including
performance, maintainability, and cost. The right answer will be different
in every situation.

In this particular example, Shoppi is a fictional startup that has built
an app for writing and managing grocery shopping lists. Shoppi is
bootstrapped. The company has 22 employees, and the app just passed
80,000 monthly subscribers at 3 USD per month. 

Shoppi has 12 engineers, 7 frontend engineers covering iOS, Android, and
web versions of the app, and 5 backend engineers covering 
authentication, data, and infrastructure, They use AWS for cloud services.

Shoppi's moat is their accumulated user list data.
While their strategy includes giving customers a friction-free
onboarding and a delightful user experience, the team believes that
the app's real stickiness will come from using past lists
to help users create new ones. This collection of user-generated list
items would be the most difficult asset for a competitor to replicate.

### Intelligent list completion

Shoppi's first step in this direction is to create a list completion feature.
Once a list is begun, the app will suggest the next five items.
Users can either accept, edit, or remove each item, after which another
suggestion is added to the list, keeping the queue at five.

If done well, these suggested items will be exactly the ones the user
had in mind, making the list creation experience faster and requiring less
mental effort. If unsuccessful, these items will be a distraction, slowing
the user down and degrading their experience.

Broadly speaking, there are three options for the algorithm behind 
making these list suggestions: A large language model (LLM), a
recommender system, or a rule-based approach. They each have areas
where they perform well and areas they struggle with. They are all
widely used. The decision of which one Shoppi should use depends
on the specifics of their situaion.

### Large Language Models

LLMs need no introduction. They are the engine behind modern AI and are
literally everywhere. Because of the passion and volume of LLM evangelists,
they are a natural solution to consider first. 

#### Simple architecture

One thing LLMs have going for themselves is that they are relatively simple
to use, if Shoppi relies on third-party models like GPT, Gemini, or Claude.
The LLMs themselves are many-billion parameter monstrosities, but third-party
providers who specialize in their training, hosting, and maintenance bear
the burden of feeding and housing them.
All Shoppi's engineers will need to do is add some
API calls to their app code. This still requires care and craft to do robustly,
but it is simpler than implementing logic or models and requires fewer
infrastructure elements. This simplicity means fewer places for bugs
to hide and fewer system compenents, which translates into shorter
development times, lower maintenance cost, and fewer failures.

#### Versatility beyond user data

The most compelling aspect of LLMs is that they have been trained on a vast
trove of data. The data certainly includes shopping lists, but also includes
recipes, parts lists for robots, sights to see in Amsterdam, baby names, and
every other type of list that has every been published on the internet.
Once a user starts writing a list, an LLM would naturally suggest a few more
items that follow along with that theme, even if no Shoppi user had ever
created a list like that before.

This versatility has strategic implications for Shoppi. Should they decide
to market their app as The Everything List creator in an effort to add
users and usage, an LLM would help them do that. But if they decide to
stay focused on grocery lists, perhaps partnering with grocery store chains to
provide discounts and build loyalty, the versatility of LLMs would be
a distractor.

#### Why not to use an LLM

Despite their strengths, LLMs have some weaknesses too. They are known
for making things up, also known as hallucination. For brainstorming a list,
this ability to think way outside the box is useful, but if
it suggests a non-existent brand of toilet paper, then it becomes
decidedly less helpful.

Using a model owned by someone else also introduces a lack of control.
If the model has security vulnerabilities or its cost suddenly jumps,
that's out of Shoppi's control. And it leaves no option for tweaking results
or adjusting the model's behavior.

Perhaps the biggest downside to using an LLM is that it takes away Shoppi's
moat. The company no longer has any strategic advantage from the customer
data it has collected. A competitor could swoop in and build a competing
app with the same performance and functionality.

### Recommender systems

Recommenders have been around since the early days of Netflix and Amazon,
well before LLMs. They are not a single thing, but a broad class of methods
that take users' past choices and use them to identify future items they
they are likely to select. In the case of shopping lists, a recommender
system would suggest items that a user has added in the past,
as well as items that other users with similar lists have added.

#### High relevance

A recommender system is naturally inclined to provide relevant suggestions,
since it is pulling from a collection of items that other users
have already deemed relevant enough to include in their own lists.
It won't invent new items from thin air.

#### Item discovery

Because it can pull from the collective history of all users' grocery items,
a recommender system can help users discover new items they are likely
to enjoy. If I have a list with potatoes and cheddar cheese, and
other users with potatoes and cheddar often add green chile to the list,
then the recommender system can suggest it, and possibly raise my baked
potato game to a new level.

#### Customizability

A recommender system often includes tweaks to get it to deliver the
right mix of relevant and novel, to avoid duplication, to steer clear
of recommending particular items, or to promote others. It can be
adapted based on business needs, design decisions, and customer feedback
to provide tailor-made distributions of suggestions. This is another
way Shoppi can transform their accumulated domain knowledge into
a wider competitive moat.

#### Why not to use a recommender system

By design, recommnder systems have several processing steps.
They are "systems" rather than "algorithms" because they typically
pull from multiple database tables and perform pre- and post-processing
on results.
They are tweakable, but that
tweakability also implies fiddling with settings and adding processing steps,
all of which adds complexity. More complexity in turn comes with more
development time and more frequent failures. This can be addressed with
careful testing and maintenance, but those come at the cost of some
developer time.

There is also a risk to user privacy when their list items can be shared
with other users. Common items are not a problem, but if a user creates
a very descriptive item or an item that includes someone's name, it could
become personally identifiable. This issue is also addressable,
but again it comes at the cost of additional pre- and post-processing,
increasing complexity.

### Rule-based suggestions

The minimum viable item recommender is a rule-based approach, for example
"Suggest the five most frequent list items from this user's history
that aren't already on the list."
The rule set can be trivially simple or extensive. Its defining characteristic
is that it's the same for everyone, all the time. It doesn't adapt
based on its experience.

#### Low latency

Rule-based suggestions can be blazingly fast to compute. 
There are no large matrices to multiply or LLMs to consult.
And for many rule sets they can also be computed locally,
on the user's device, making them even snappier.

#### Low computation cost

The lightweight computation requirements also come at lower cost.
There are fewer FLOPs and less memory, which means they can be run on
fewer, smaller, and cheaper computers.

#### Transparency (explainability and debuggability)

As a bonus, rule-based approaches are entirely transparent. Every decision
for what to recommend can be traced back to the rule responsible.
Debugging undesired behaviors becomes straightforward, as does modifying
the rules to change those behaviors.

#### Why not to use a rule-based system

The only downside to rule-based recommendations is that they are narrow
and brittle. They are limited to the cases that the creators can foresee.
It's usually possible to find corner cases and combinations where the
recommendations fail or become ridiculous. Maintaining them can become
a game of Whac-A-Mole where a new rule gets added for every bug observed
in production.

## Analysis

The Shoppi team is in search of an approach that is consistent
with their strategy of providing a seamless user experience,
and one that is compatible with their current size and capabilities.
Their wish list for a solution includes several
performance and implementation characteristics.

- $whitecircle$ ok
- $lowerhalfblackcircle$ better
- $blackcircle$ best

|                           | Rule-based | Recommender | LLM |
|-----|-----|-----|-----|
|Relevance of results       | $whitecircle$ | $blackcircle$ | $lowerhalfblackcircle$ |
|Absence of obvious mistakes| $blackcircle$ | $blackcircle$ | $whitecircle$ |
|Snappy response            | $blackcircle$ | $lowerhalfblackcircle$ | $whitecircle$ |
|Short time to build        | $lowerhalfblackcircle$ | $whitecircle$ | $blackcircle$ |
|Ability to improve         | $blackcircle$ | $lowerhalfblackcircle$ | $whitecircle$ |
|Predictability and control | $blackcircle$ | $lowerhalfblackcircle$ | $whitecircle$ |
|Low cost to maintain       | $blackcircle$ | $whitecircle$ | $lowerhalfblackcircle$ |

#### Relevance of results

A perfect solution will generate exactly the item suggestions
that the user is intending to add next, or that they might have forgotten,
or that would have added if they had known about them.
The recommendations will feel like those of a personal assistant who
knows the user's preferences well and is knowledgeable about the
avilable options.

Recommender systems are the winners here. They are designed from the
ground up to do exactly this. First-time users get the benefit of every
list that every other user made before. Repeat users get the bonus
of their own past list-making history. A well designed recommender system
can make the most of this data to provide highly relevant recommendations.

LLMs are strong in this area for first-time users as well. Thanks
to the vast data sets on which they are trained, they are surprisingly
good at finding the most natural next item in a sequence. They require
more tweaking to incorporate users' past lists, in an implementation
variation called Retrieval-Augmented Generation (RAG), but this
is feasible to do as well. And for users making non-grocery lists,
LLMs will happily supply items that follow whatever pattern they
establish when they start their list.

A rule-based approach brings up the rear in this category. With clever
heuristics and a long enough set of checks and conditions, rule-based
suggestions can be quite good, but they are likely to have blind spots
and be sensitive to small changes.

#### Absence of obvious mistakes

If a suggested list item is out of place, ridiculous, or garbled it makes for
a jarring user experience. It will interrupt the flow of their task,
precisely the opposite of Shoppi's intent. It can also make for
embarassing screen shots on social media. 

Recommender systems and rule-based approaches are tied for first place
on this one. Both of these approaches rely on actual list items that
users have typed in with their own fingers. This is a powerful filter,
especially after eliminating items that only occur once or twice.

LLMs however are notorious for making things up (euphemistially referred
to as hallucinating). Careful prompting and extra checks on the output
can minimize this, but so far there is no way to eliminate it. And
adversarial users can often find a way to break them by co-opting
fake list items to over-write the LLM's instructions. These vulnerabilities
are frequently called out under the caveat "Generated by AI" in LLM-powered
products, but even though this is common in the industry, Shoppi will
need to decide whether this is the experience they want for their users.

#### Snappy response

The snappiness of the feature is determined by the latency, how long
the user has to wait between accepting an item and seeing the next
recommendation. Rule based approaches are the clear winner here,
especially if the engineering team goes to the extra work to have them
run on the device. The calculations involved are not complex, and even
a long list of rules can be handled so quickly as to feel instantaneous.

Recommender systems typically take a  bit longer, but are still quick.
They normally involve multiple network calls and often require some
matrix multiplication, but even so they tend to do their job in the
10s-to-100s of milliseconds range. Just long enough to be noticeable,
but not so long that it's annoying. The experience is more a speed bump
than a stoplight.

LLMs Bring up the rear in this category. It’s common for them to have
latencies of a second or more. This feels sluggish and can have an
negative effect on the user experience.

#### Short time to build

A short time to build is doubly desirable. It means a smaller investment
of engineering time and a shorter delay before benefits of the new future
can be realized. A basic implementation of LLMs has the shortest build time
of the bunch. It can be implemented with an API call from the app.
All the model training and hosting is handled by the model provider.

Rule-based approaches take only a little longer to implement, especially
for a simple rule set. Since past list items are already stored,
rules can access them directly and use them to populate suggestions.

Recommender systems take the longest time to build. While there are
libraries and templates, most of the advantages of recommender systems
come from customizing them to your own use case and data. The effort required
to build and maintain a modern recommendation system can be monumental,
but there are simpler variants that would make more sense for Shoppi
to start with where the required effort would be more reasonable.

#### Ability to improve

There are guaranteed to be cases where the Shoppi team will want to adjust
to the results, either to respond to direct user feedback, or to remove
items from the recommendation pool that may be discontinued, or to steer
recommendations toward branded items instead of generic ones.
A rule-based approach has the capability to do this quickly, often
by changing a couple lines of code. They have the added benefit that
the source of any undesirable recommendation is straightforward to identify.
The net result is that they are easy to improve.

Recommender systems are also highly customizable, although getting them
to produce a particular recommendation can be fiddly. Typically,
it requires someone with an in-depth understanding of how the recommender
works. However, once in the hands of an expert, a recommender system can be
adapted and adjusted in ways that would be difficult for a rule-based
system to emulate. They are trickier to work with but have more
expansive capabilities.

LLMs are the least easy to improve of the three. The underlying model is
pre-trained and not available for modification. A lot can be done to steer
the model's output by adding extra instructions in the prompt, but this
approach is even less deterministic than modifying recommender systems.
Changes can have unintended consequences. Adding prompt instructions to
affect one category of suggestions can end up changing another
unrelated category for no apparent reason. Getting it to behave just right
is an art and can require a great deal of trial, error, and patience.

#### High predictability and control

When you want to make confident statements about the performance, costs,
and relevance of the results, greater level of control is helpful.
Due to their simplicity, the rule-based approach is the most predictable
and offers the greatest level of control. It is architecturally boring,
but that is an asset when it comes to determinism and reliability.

By virtue of their complexity, recommender systems are less predictable
than rule-based. Even though every aspect of the system is observable
in theory, the way they interact can be complicated and challenging to
instrument and interpret. However, costs are likely to scale predictably
with the volume of queries, making it possible to do financial estimation well.

LLMs are the least predictable of the available options. They have
randomness built into them by nature, and it’s impossible to inspect them
directly to determine why they are giving a particular recommendation.
However, the more fundamental control issue is that the model is controlled
entirely by another entity. If issues arise with quality of results,
latency, or availability then there’s nothing that can be done except
raise a ticket with the customer service teams at Google or OpenAI.
Over the longer term, there are no guarantees about how pricing will
change six or twelve months, or even whether a particular model will
still be available. All of these are problems that can be solved,
but they are good to be aware of before building LLM’s into a core feature.

#### Low cost to maintain

Thanks to its architectural simplicity, a rule based approach is the
least expensive to maintain. There are very few moving parts that can break.
If and when any bugs do occur, it is transparent and straightforward
to debug. The computational cost for operation is negligible.

LLMs Have a modest maintenance cost. There is a small cost based on
its length. Luckily the queries involved in grocery list completion are
relatively short. These can add up if there are a large number of them,
but the cost per user will remain small. The larger factor in LLM
maintenance costs is the overhead from ensuring that calls to the model are
successful and that there is a graceful failure path when they are not.
LLM API’s are fairly reliable, but not perfect. Unsuccessful calls happen
often enough that a good product will be able to handle them. These
monitoring and fallback systems need not be overly complex, but it does
take a little time and effort to do them well.

The complexity of recommender systems means that the monitoring,
failure handling, and system maintenance effort is many times greater.
While the details depend entirely on the specifics of the particular system,
a medium-sized recommender system is likely to demand at least half-time
attention from a machine learning engineer. Maintenance costs for
a recommender system are relatively high.

### Decision

There is not just one option that checks all the boxes. To settle on an answer,
the Shoppi team has to choose which aspect are most important to them.

After some clear-eyed introspection, Shoppi leaders came to the difficult
conclusion that they care more about long-term sustainable success
than quick growth. Their chief strategic concern is maintaining their
competitive advantage over future competitors and widening
their moat--their collect history of users' past grocery list items.

Although they provide quick short-term progress, LLMs do not take advantage
of users' histories in the way rule-based and recommender systems do.
The team decided to set LLMs aside for now and re-evaluate their usefulness
in 6-12 months, by which time both the business needs and LLM capabilities
will probably have evolved.
Shoppi is free to do this, since they are bootstrapped. They 
have no venture capital investors to please, who might push Shoppi to use LLMs
for reasons of their own.

Between rule-based and recommender systems, the short time to build and
low maintenance costs of a **rule-based approach** make it the front runner.
Shoppi's engineering team is already running lean and does not have the
capacity for the large development effort that a recommender system would
require. Even more challenging, the team doesn't yet have the necessary
expertise to build it. Embarking on a recommender system creation effort
will probably require a specialized hire to create and maintain it.

Rule-based item recommendations give the team an opportunity to test
the value of the feature, and assess whether it is worth making a bigger
investment in 12-18 months in order to generate more relevant recommendations.
They anticipate that is also the timeframe in which they will explore
partnerships with grocery store chains, and having a recommender system
will let them track and guarantee user exposure to store brands and
coupons.

### The Big Picture

Taking a step back, the decision of the imaginary Shoppi team to use a
rule-based approach is very specific to their needs and priorities.
The point of this analysis is not to argue that one particular
approach is superior,
but to show the strengths and weaknesses of each option
and the process of evaluating them.

Trade-offs rule every technical decision we make. We always have to
give up things we want for things we want more. The ability to do this
with clarity and confidence will set your team apart and keep you
from getting bogged down in indecision and divided effort.

If you find your team weighing a strategic technical decision like this
and would like a fresh pair of eyes to help you evaluate it,
drop me a line at
[brandon@brandonrohrer.com](mailto:brandon@brandonrohrer.com).

Special thanks to Karl Higley for reading through this and giving me
some helpful feedback on recommender systems.
-----

I work with tech leaders in small and medium-sized companies
to navigate all aspects of data, analytics, and machine learning.

If you'd like a note when the next post comes out, email me at
[posts@brandonrohrer.com
](mailto:posts@brandonrohrer.com?subject=Future%20posts&body=Please%20let%20me%20know%20when%20the%20next%20one%20comes%20out.)
