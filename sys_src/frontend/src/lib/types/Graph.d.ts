export default interface State {
  hoveredNode?: string;
  searchQuery: string;
  selectedNode?: string;
  hoveredNodeNeighbors?: Set<string>;
}