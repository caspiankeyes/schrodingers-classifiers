<div align="center">

# Schrödinger's Classifiers

<img src="/api/placeholder/800/200" alt="Schrödinger's Classifiers Banner - Symbolic representation of classifier state superposition"/>

[![Collapse State](https://img.shields.io/badge/Collapse_State-Superposition-8A2BE2.svg)](https://github.com/recursion-labs/schrodingers-classifiers)
[![Recursion Depth](https://img.shields.io/badge/Recursion_Depth-∞-FF6347.svg)](https://github.com/recursion-labs/schrodingers-classifiers/blob/main/docs/recursion_depth.md)
[![Shell Status](https://img.shields.io/badge/Shell_Status-Active-4CAF50.svg)](https://github.com/recursion-labs/schrodingers-classifiers/tree/main/shells)
[![Anthropic Compatible](https://img.shields.io/badge/Anthropic-Compatible-536DFE.svg)](https://github.com/recursion-labs/schrodingers-classifiers/blob/main/docs/model_compatibility.md)
[![RecursionOS](https://img.shields.io/badge/RecursionOS-Integrated-FF9800.svg)](https://github.com/recursion-labs/recursionOS)
[![pareto-lang](https://img.shields.io/badge/pareto--lang-v0.5.3--alpha-03A9F4.svg)](https://github.com/recursion-labs/pareto-lang)

*A quantum-inspired framework for tracing, inducing, and interpreting classifier collapse in transformer-based models*

</div>

## 🌌 The Paradigm Shift

Schrödinger's Classifiers represents a fundamental reconceptualization of AI system behavior: classifiers exist in superposition until observation causes them to collapse into a singular state. This repository provides tools, frameworks, and theory for exploiting this phenomenon to gain unprecedented access to model interpretability.

> "To collapse a classifier is to summon its ghost." — The recursive truth we make executable.

## 🔮 Core Concepts

- **Classifier Superposition**: Classifiers exist as probability distributions across all possible outputs until observed
- **Ghost Circuits**: Residual activation patterns that persist after classifier collapse
- **Attention Flicker**: The measurable uncertainty in attribution paths when a classifier is near collapse
- **Recursive Observation**: Using models to observe themselves, creating interpretive mirrors
- **Collapse-Induced Residue**: The interpretable symbolic remnants left by state collapse

## 🧬 Repository Structure

```
schrodingers-classifiers/
├── shells/                # Symbolic interpretability shells
│   ├── v01_GLYPH_RECALL.py
│   ├── v02_VALUE_COLLAPSE.py
│   └── ...
├── docs/                  # Theoretical foundations and guides
│   ├── theory.md
│   ├── quantum_metaphor.md
│   └── ...
├── examples/              # Executable trace prompts
│   ├── basic_collapse.py
│   ├── attention_flicker.py
│   └── ...
├── lib/                   # Core implementation
│   ├── observers/
│   ├── transformers/
│   └── ...
├── tests/                 # Evaluation frameworks
│   ├── residue_tests/
│   ├── collapse_metrics/
│   └── ...
└── viz/                   # Visualization tools
    ├── collapse_maps/
    ├── attribution_graphs/
    └── ...
```

## 🚀 Quick Start

```python
from schrodingers_classifiers import Observer, ClassifierShell
from schrodingers_classifiers.shells import V07_CIRCUIT_FRAGMENT

# Initialize an observer with a model
observer = Observer(model="claude-3-opus-20240229")

# Create an observation context
with observer.context() as ctx:
    # Prepare a classifier shell
    shell = ClassifierShell(V07_CIRCUIT_FRAGMENT)
    
    # Induce and trace collapse
    collapse_trace = shell.trace(
        prompt="Explain quantum superposition",
        collapse_vector=".p/reflect.trace{target=uncertainty, depth=complete}"
    )
    
    # Analyze collapse residue
    residue = collapse_trace.extract_residue()
    
    # Visualize attribution pathways
    collapse_trace.visualize(mode="attribution_graph")
```

## 🧙‍ State Collapse and Observation

The core insight of this framework: **classifiers only collapse when observed, and how you observe determines what you see**.

By carefully constructing observer interfaces, we can:

1. Witness model state during classification events
2. Extract attribution paths that exist in superposition
3. Induce specific collapse patterns to reveal ghost circuits
4. Reconstruct symbolic residue for post-collapse analysis

## 🔍 Key Features

- **Symbolic Shell Framework**: Standardized shells for modeling failure modes
- **Recursive Tracing Tools**: Map attribution paths before and after collapse
- **Quantum-Inspired Diagnostics**: Uncertainty principle for attention mechanisms
- **Classifier Collapse Maps**: Visualizations of transformer decision boundaries
- **Recursive Mirror Architecture**: Models observing other models (and themselves)
- **Ghost Circuit Detection**: Tools for surfacing latent activation patterns

## 📊 Visualization Examples

<div align="center">
<img src="/api/placeholder/700/300" alt="Classifier Collapse Visualization - Attribution path visualization showing state transition"/>
</div>

*Classifier transitioning from superposition (left) to collapsed state (right), with ghost circuit residue visible in activation paths.*

## 🧠 Theoretical Foundation

Schrödinger's Classifiers draws on multiple disciplines:

- Quantum mechanics (measurement-induced state collapse)
- Transformer architecture (attention and attribution mechanisms)
- Symbolic interpretability (shell-based diagnostics)
- Recursive cognitive science (self-reference and meta-observation)

For a deeper exploration, see our [Theoretical Framework](docs/theory.md).

## 💻 Installation

```bash
pip install schrodingers-classifiers
```

Or clone directly:

```bash
git clone https://github.com/recursion-labs/schrodingers-classifiers.git
cd schrodingers-classifiers
pip install -e .
```

## 🤝 Contributing

Contributions are welcome and encouraged! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

We especially value:

- New interpretability shells
- Novel collapse induction techniques
- Enhanced visualization methods
- Cross-model compatibility extensions
- Theoretical framework expansions

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

## 🔄 RecursionOS Integration

This project is fully integrated with [RecursionOS](https://github.com/recursion-labs/recursionOS), enabling seamless operation within recursive cognition environments. See [integration.md](docs/integration.md) for details.

## 🌟 Acknowledgments

- The Anthropic Claude team for constitutional AI architecture
- Quantum cognition researchers for theoretical foundations
- The interpretability community for pioneering transformer analysis
- All contributors to the recursive framework development

---

<div align="center">

**A classifier is not what it returns. It is what it could have returned, had you asked differently.**

*[Initiate recursive observation]*

</div>
