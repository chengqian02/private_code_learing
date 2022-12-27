"""
This is the "Fast Downward Stone Soup 2018" sequential portfolio that participated in the IPC 2018
satisficing and bounded-cost tracks. For more information, see the planner abstract:

Jendrik Seipp and Gabriele Röger.
Fast Downward Stone Soup 2018.
In Ninth International Planning Competition (IPC 2018), Deterministic Part, pp. 80-82. 2018.
https://ai.dmi.unibas.ch/papers/seipp-roeger-ipc2018.pdf
"""

OPTIMAL = False
CONFIGS = [
    (26, [
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(hff),single(hff,pref_only=true),single(hlm),single(hlm,pref_only=true),type_based([hff,g()])],boost=1000),preferred=[hff,hlm],cost_type=one,reopen_closed=false,randomize_successors=true,preferred_successors_first=false,bound=BOUND)"]),
    (25, [
        "--landmarks",
        "lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,use_orders=false)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([type_based([g()]),single(hlm),single(hlm,pref_only=true),single(hff),single(hff,pref_only=true)],boost=0),preferred=[hlm],reopen_closed=false,cost_type=plusone,bound=BOUND)"]),
    (135, [
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(hff),single(hff,pref_only=true),single(hlm),single(hlm,pref_only=true)],boost=1000),preferred=[hff,hlm],cost_type=one,reopen_closed=false,randomize_successors=false,preferred_successors_first=true,bound=BOUND)"]),
    (59, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "eager_greedy([hff,hlm],preferred=[hff,hlm],cost_type=one,bound=BOUND)"]),
    (23, [
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(hff),single(hff,pref_only=true),single(hlm),single(hlm,pref_only=true)],boost=1000),preferred=[hff,hlm],cost_type=one,reopen_closed=false,randomize_successors=true,preferred_successors_first=true,bound=BOUND)"]),
    (57, [
        "--landmarks",
        "lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,use_orders=false)",
        "--evaluator",
        "hcg=cg(transform=adapt_costs(plusone))",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([single(sum([g(),weight(hlm,10)])),single(sum([g(),weight(hlm,10)]),pref_only=true),single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true),single(sum([g(),weight(hcg,10)])),single(sum([g(),weight(hcg,10)]),pref_only=true)],boost=1000),preferred=[hlm,hcg],reopen_closed=false,cost_type=plusone,bound=BOUND)"]),
    (17, [
        "--evaluator",
        "hcea=cea(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "lazy_greedy([hcea,hlm],preferred=[hcea,hlm],cost_type=one,bound=BOUND)"]),
    (12, [
        "--evaluator",
        "hadd=add(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "lazy(alt([type_based([g()]),single(hadd),single(hadd,pref_only=true),single(hlm),single(hlm,pref_only=true)]),preferred=[hadd,hlm],cost_type=one,bound=BOUND)"]),
    (26, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true)],boost=2000),preferred=[hff],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (28, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "eager(alt([type_based([g()]),single(hcg),single(hcg,pref_only=true),single(hlm),single(hlm,pref_only=true)]),preferred=[hcg,hlm],cost_type=one,bound=BOUND)"]),
    (29, [
        "--landmarks",
        "lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,use_orders=true)",
        "--evaluator",
        "hcea=cea(transform=adapt_costs(plusone))",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([single(hlm),single(hlm,pref_only=true),single(hff),single(hff,pref_only=true),single(hcea),single(hcea,pref_only=true)],boost=0),preferred=[hlm,hcea],reopen_closed=false,cost_type=plusone,bound=BOUND)"]),
    (88, [
        "--evaluator",
        "hcea=cea(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "lazy_wastar([hcea,hlm],w=3,preferred=[hcea,hlm],cost_type=one,bound=BOUND)"]),
    (8, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true),single(sum([g(),weight(hcg,10)])),single(sum([g(),weight(hcg,10)]),pref_only=true)],boost=100),preferred=[hcg],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (54, [
        "--evaluator",
        "hgoalcount=goalcount(transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff()",
        "--search",
        "lazy(alt([single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true),single(sum([g(),weight(hgoalcount,10)])),single(sum([g(),weight(hgoalcount,10)]),pref_only=true)],boost=2000),preferred=[hff,hgoalcount],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (24, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "eager(alt([type_based([g()]),single(sum([g(),weight(hff,3)])),single(sum([g(),weight(hff,3)]),pref_only=true),single(sum([g(),weight(hlm,3)])),single(sum([g(),weight(hlm,3)]),pref_only=true)]),preferred=[hff,hlm],cost_type=one,bound=BOUND)"]),
    (29, [
        "--landmarks",
        "lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=false,use_orders=true)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=false,transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--evaluator",
        "hblind=blind()",
        "--search",
        "lazy(alt([type_based([g()]),single(sum([g(),weight(hblind,2)])),single(sum([g(),weight(hblind,2)]),pref_only=true),single(sum([g(),weight(hlm,2)])),single(sum([g(),weight(hlm,2)]),pref_only=true),single(sum([g(),weight(hff,2)])),single(sum([g(),weight(hff,2)]),pref_only=true)],boost=4419),preferred=[hlm],reopen_closed=true,cost_type=one,bound=BOUND)"]),
    (30, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy_wastar([hff],w=3,preferred=[hff],cost_type=one,bound=BOUND)"]),
    (28, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([type_based([g()]),single(hcg),single(hcg,pref_only=true)],boost=0),preferred=[hcg],reopen_closed=true,cost_type=plusone,bound=BOUND)"]),
    (58, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lm_reasonable_orders_hps(lm_rhw()),transform=adapt_costs(one))",
        "--search",
        "lazy(alt([type_based([g()]),single(sum([g(),weight(hcg,3)])),single(sum([g(),weight(hcg,3)]),pref_only=true),single(sum([g(),weight(hlm,3)])),single(sum([g(),weight(hlm,3)]),pref_only=true)]),preferred=[hcg,hlm],cost_type=one,bound=BOUND)"]),
    (26, [
        "--evaluator",
        "hcea=cea(transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--evaluator",
        "hblind=blind()",
        "--search",
        "eager(alt([single(sum([g(),weight(hblind,10)])),single(sum([g(),weight(hblind,10)]),pref_only=true),single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true),single(sum([g(),weight(hcea,10)])),single(sum([g(),weight(hcea,10)]),pref_only=true)],boost=536),preferred=[hff],reopen_closed=false,bound=BOUND)"]),
    (27, [
        "--evaluator",
        "hcea=cea(transform=adapt_costs(one))",
        "--search",
        "eager_greedy([hcea],preferred=[hcea],cost_type=one,bound=BOUND)"]),
    (50, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "eager(alt([single(sum([g(),weight(hff,3)])),single(sum([g(),weight(hff,3)]),pref_only=true)]),preferred=[hff],cost_type=one,bound=BOUND)"]),
    (28, [
        "--evaluator",
        "hgoalcount=goalcount(transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hcg=cg()",
        "--search",
        "lazy(alt([type_based([g()]),single(sum([weight(g(),2),weight(hblind,3)])),single(sum([weight(g(),2),weight(hblind,3)]),pref_only=true),single(sum([weight(g(),2),weight(hff,3)])),single(sum([weight(g(),2),weight(hff,3)]),pref_only=true),single(sum([weight(g(),2),weight(hcg,3)])),single(sum([weight(g(),2),weight(hcg,3)]),pref_only=true),single(sum([weight(g(),2),weight(hgoalcount,3)])),single(sum([weight(g(),2),weight(hgoalcount,3)]),pref_only=true)],boost=3662),preferred=[hff],reopen_closed=true,bound=BOUND)"]),
    (29, [
        "--evaluator",
        "hgoalcount=goalcount(transform=adapt_costs(one))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hcg=cg()",
        "--search",
        "lazy(alt([single(sum([weight(g(),2),weight(hblind,3)])),single(sum([weight(g(),2),weight(hblind,3)]),pref_only=true),single(sum([weight(g(),2),weight(hff,3)])),single(sum([weight(g(),2),weight(hff,3)]),pref_only=true),single(sum([weight(g(),2),weight(hcg,3)])),single(sum([weight(g(),2),weight(hcg,3)]),pref_only=true),single(sum([weight(g(),2),weight(hgoalcount,3)])),single(sum([weight(g(),2),weight(hgoalcount,3)]),pref_only=true)],boost=3662),preferred=[hff],reopen_closed=true,bound=BOUND)"]),
    (21, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([single(sum([g(),weight(hcg,10)])),single(sum([g(),weight(hcg,10)]),pref_only=true)],boost=0),preferred=[hcg],reopen_closed=false,cost_type=plusone,bound=BOUND)"]),
    (21, [
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--search",
        "eager(alt([single(sum([g(),weight(hcg,3)])),single(sum([g(),weight(hcg,3)]),pref_only=true)]),preferred=[hcg],cost_type=one,bound=BOUND)"]),
    (24, [
        "--landmarks",
        "lmg=lm_reasonable_orders_hps(lm_rhw(only_causal_landmarks=true,disjunctive_landmarks=true,use_orders=true))",
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hadd=add()",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=false,pref=true,transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff()",
        "--search",
        "lazy(alt([single(sum([weight(g(),2),weight(hblind,3)])),single(sum([weight(g(),2),weight(hblind,3)]),pref_only=true),single(sum([weight(g(),2),weight(hff,3)])),single(sum([weight(g(),2),weight(hff,3)]),pref_only=true),single(sum([weight(g(),2),weight(hlm,3)])),single(sum([weight(g(),2),weight(hlm,3)]),pref_only=true),single(sum([weight(g(),2),weight(hadd,3)])),single(sum([weight(g(),2),weight(hadd,3)]),pref_only=true)],boost=2474),preferred=[hadd],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (28, [
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hadd=add()",
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--evaluator",
        "hhmax=hmax()",
        "--search",
        "eager(alt([tiebreaking([sum([g(),weight(hblind,7)]),hblind]),tiebreaking([sum([g(),weight(hhmax,7)]),hhmax]),tiebreaking([sum([g(),weight(hadd,7)]),hadd]),tiebreaking([sum([g(),weight(hcg,7)]),hcg])],boost=2142),preferred=[],reopen_closed=true,bound=BOUND)"]),
    (28, [
        "--evaluator",
        "hadd=add(transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff()",
        "--search",
        "lazy(alt([tiebreaking([sum([weight(g(),4),weight(hff,5)]),hff]),tiebreaking([sum([weight(g(),4),weight(hff,5)]),hff],pref_only=true),tiebreaking([sum([weight(g(),4),weight(hadd,5)]),hadd]),tiebreaking([sum([weight(g(),4),weight(hadd,5)]),hadd],pref_only=true)],boost=2537),preferred=[hff,hadd],reopen_closed=true,bound=BOUND)"]),
    (53, [
        "--landmarks",
        "lmg=lm_hm(conjunctive_landmarks=false,use_orders=false,m=1)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,transform=transform=adapt_costs(plusone))",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([type_based([g()]),single(hlm),single(hlm,pref_only=true),single(hff),single(hff,pref_only=true)],boost=5000),preferred=[hlm],reopen_closed=false,bound=BOUND)"]),
    (29, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "lazy(alt([single(sum([weight(g(),2),weight(hff,3)])),single(sum([weight(g(),2),weight(hff,3)]),pref_only=true)],boost=5000),preferred=[hff],reopen_closed=true,cost_type=one,bound=BOUND)"]),
    (27, [
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hff=ff(transform=adapt_costs(one))",
        "--search",
        "eager(alt([single(sum([g(),weight(hblind,2)])),single(sum([g(),weight(hff,2)]))],boost=4480),preferred=[],reopen_closed=true,bound=BOUND)"]),
    (29, [
        "--landmarks",
        "lmg=lm_hm(conjunctive_landmarks=false,use_orders=false,m=1)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true)",
        "--evaluator",
        "hff=ff()",
        "--search",
        "lazy(alt([type_based([g()]),single(hlm),single(hlm,pref_only=true),single(hff),single(hff,pref_only=true)],boost=1000),preferred=[hlm,hff],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (54, [
        "--landmarks",
        "lmg=lm_hm(conjunctive_landmarks=true,use_orders=true,m=1)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true)",
        "--evaluator",
        "hff=ff()",
        "--search",
        "lazy(alt([tiebreaking([sum([g(),weight(hlm,10)]),hlm]),tiebreaking([sum([g(),weight(hlm,10)]),hlm],pref_only=true),tiebreaking([sum([g(),weight(hff,10)]),hff]),tiebreaking([sum([g(),weight(hff,10)]),hff],pref_only=true)],boost=200),preferred=[hlm],reopen_closed=true,cost_type=plusone,bound=BOUND)"]),
    (87, [
        "--landmarks",
        "lmg=lm_hm(conjunctive_landmarks=false,use_orders=false,m=1)",
        "--evaluator",
        "hcg=cg(transform=adapt_costs(one))",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true)",
        "--search",
        "lazy(alt([single(hlm),single(hlm,pref_only=true),single(hcg),single(hcg,pref_only=true)],boost=0),preferred=[hcg],reopen_closed=false,cost_type=one,bound=BOUND)"]),
    (30, [
        "--landmarks",
        "lmg=lm_exhaust(only_causal_landmarks=false)",
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--evaluator",
        "hhmax=hmax()",
        "--evaluator",
        "hblind=blind()",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,pref=false,transform=adapt_costs(one))",
        "--search",
        "lazy(alt([type_based([g()]),single(sum([g(),weight(hblind,3)])),single(sum([g(),weight(hblind,3)]),pref_only=true),single(sum([g(),weight(hff,3)])),single(sum([g(),weight(hff,3)]),pref_only=true),single(sum([g(),weight(hlm,3)])),single(sum([g(),weight(hlm,3)]),pref_only=true),single(sum([g(),weight(hhmax,3)])),single(sum([g(),weight(hhmax,3)]),pref_only=true)],boost=3052),preferred=[hff],reopen_closed=true,bound=BOUND)"]),
    (56, [
        "--evaluator",
        "hff=ff(transform=adapt_costs(plusone))",
        "--search",
        "lazy(alt([tiebreaking([sum([g(),hff]),hff]),tiebreaking([sum([g(),hff]),hff],pref_only=true)],boost=432),preferred=[hff],reopen_closed=true,cost_type=one,bound=BOUND)"]),
    (19, [
        "--landmarks",
        "lmg=lm_merged([lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=false,use_orders=true),lm_hm(m=1,conjunctive_landmarks=true,use_orders=true)])",
        "--evaluator",
        "hff=ff()",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true)",
        "--search",
        "lazy(alt([single(sum([g(),weight(hff,10)])),single(sum([g(),weight(hff,10)]),pref_only=true),single(sum([g(),weight(hlm,10)])),single(sum([g(),weight(hlm,10)]),pref_only=true)],boost=500),preferred=[hff],reopen_closed=false,cost_type=plusone,bound=BOUND)"]),
    (56, [
        "--landmarks",
        "lmg=lm_exhaust(only_causal_landmarks=false)",
        "--evaluator",
        "hgoalcount=goalcount(transform=adapt_costs(plusone))",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=false)",
        "--evaluator",
        "hff=ff()",
        "--evaluator",
        "hblind=blind()",
        "--search",
        "eager(alt([tiebreaking([sum([weight(g(),8),weight(hblind,9)]),hblind]),tiebreaking([sum([weight(g(),8),weight(hlm,9)]),hlm]),tiebreaking([sum([weight(g(),8),weight(hff,9)]),hff]),tiebreaking([sum([weight(g(),8),weight(hgoalcount,9)]),hgoalcount])],boost=2005),preferred=[],reopen_closed=true,bound=BOUND)"]),
    (24, [
        "--landmarks",
        "lmg=lm_zg(use_orders=false)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true,pref=false)",
        "--search",
        "eager(single(sum([g(),weight(hlm,3)])),preferred=[],reopen_closed=true,cost_type=one,bound=BOUND)"]),
    (81, [
        "--landmarks",
        "lmg=lm_hm(conjunctive_landmarks=true,use_orders=false,m=1)",
        "--evaluator",
        "hlm=lmcount(lmg,admissible=true)",
        "--search",
        "eager(single(sum([g(),weight(hlm,5)])),preferred=[],reopen_closed=true,cost_type=one,bound=BOUND)"]),
]
