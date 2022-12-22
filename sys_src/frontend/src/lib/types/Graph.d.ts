export default interface State {
  searchQuery: string;
  hoveredNode?: string;
  selectedNode?: string;
  hoveredNodeNeighbors?: Set<string>;
}