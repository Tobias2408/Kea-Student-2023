import { Router } from "express";
const router = Router();

const users = [{
    id: 1,
    name: "John Doe"
}];

const spaceCrafts = [{
    id: 1,
    description: "SpaceCraft1"
    
}];

/**
 * @openapi
 * /api/users:
 *   get:
 *     description: Get all users
 *     responses:
 *       200:
 *         description: Returns all users
 */
router.get("/api/users", (req, res) => {
    res.send({ data: users });
});

/**
 * @openapi
 * /api/users:
 *   post:
 *     description: Create a new user
 *     responses:
 *       200:
 *         description: Returns the users that was created
 */
router.post("/api/users", (req, res) => {
    const user = req.body;
    users.push(user);
    res.send({ data: user });
});
router.get("/api/spacecrafts", (req, res) => {
    res.send({ data: spaceCrafts });
});

router.get("/api/spacecrafts/:spacecraftId", (req, res) => {
    console.log(req.params.spacecraftId)
    res.send({data:spaceCrafts.find(x => x.id = req.params.spacecraftId)});
});
    

export default router;