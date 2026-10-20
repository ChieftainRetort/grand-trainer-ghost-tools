const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("ghostBridge", {
  spiritState: "dormant",
  trainerFlags: [],
  ghostCount: 0,
});