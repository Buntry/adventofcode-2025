use std::collections::{HashMap, VecDeque};

pub fn solve(input: &str) {    
    let graph = parse_input(input);
    
    let part1 = solve_part1(&graph);
    println!("Part 1: {}", part1);

    // let part2 = solve_part2(&graph);
    // println!("Part 2: {}", part2);
}

fn parse_input(input: &str) -> HashMap<String, Vec<String>> {
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();
    
    for line in input.lines() {
        if let Some((source, targets)) = line.split_once(": ") {
            let targets: Vec<String> = targets
                .split_whitespace()
                .map(|s| s.to_string())
                .collect();
            graph.insert(source.to_string(), targets);
        }
    }
    graph
}

fn solve_part1(graph: &HashMap<String, Vec<String>>) -> usize {
    let paths = find_all_paths(graph, "you", "out");
    paths.len()
}

fn find_all_paths(graph: &HashMap<String, Vec<String>>, start: &str, end: &str,) -> Vec<Vec<String>> {
    let mut all_paths: Vec<Vec<String>> = Vec::new();
    let mut queue: VecDeque<Vec<String>> = VecDeque::new();
    
    queue.push_back(vec![start.to_string()]);
    
    while let Some(current_path) = queue.pop_front() {
        let current_node = current_path.last().unwrap();
        
        if current_node == end {
            all_paths.push(current_path);
            continue;
        }
        
        if let Some(neighbors) = graph.get(current_node) {
            for neighbor in neighbors {
                if current_path.contains(neighbor) {
                    continue;
                }
                
                let mut new_path = current_path.clone();
                new_path.push(neighbor.clone());
                queue.push_back(new_path);
            }
        }
    }
    
    all_paths
}