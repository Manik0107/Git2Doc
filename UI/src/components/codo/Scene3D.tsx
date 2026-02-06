import { useRef, useMemo } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Float, MeshDistortMaterial } from "@react-three/drei";
import * as THREE from "three";

const FloatingShape = ({ 
  position, 
  scale, 
  speed, 
  rotationSpeed,
  distort 
}: { 
  position: [number, number, number]; 
  scale: number; 
  speed: number;
  rotationSpeed: number;
  distort: number;
}) => {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.x += rotationSpeed * 0.01;
      meshRef.current.rotation.y += rotationSpeed * 0.015;
      meshRef.current.position.y += Math.sin(state.clock.elapsedTime * speed) * 0.002;
    }
  });

  return (
    <Float speed={speed} rotationIntensity={0.5} floatIntensity={1}>
      <mesh ref={meshRef} position={position} scale={scale}>
        <icosahedronGeometry args={[1, 1]} />
        <MeshDistortMaterial
          color="#ff1a1a"
          emissive="#330000"
          emissiveIntensity={0.5}
          roughness={0.2}
          metalness={0.8}
          distort={distort}
          speed={2}
        />
      </mesh>
    </Float>
  );
};

const FloatingTorus = ({ 
  position, 
  scale, 
  speed 
}: { 
  position: [number, number, number]; 
  scale: number; 
  speed: number;
}) => {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.x = state.clock.elapsedTime * speed * 0.3;
      meshRef.current.rotation.z = state.clock.elapsedTime * speed * 0.2;
    }
  });

  return (
    <Float speed={speed * 0.5} rotationIntensity={1} floatIntensity={0.5}>
      <mesh ref={meshRef} position={position} scale={scale}>
        <torusGeometry args={[1, 0.3, 16, 32]} />
        <meshStandardMaterial
          color="#cc0000"
          emissive="#1a0000"
          emissiveIntensity={0.3}
          roughness={0.3}
          metalness={0.9}
        />
      </mesh>
    </Float>
  );
};

const FloatingOctahedron = ({ 
  position, 
  scale, 
  speed 
}: { 
  position: [number, number, number]; 
  scale: number; 
  speed: number;
}) => {
  const meshRef = useRef<THREE.Mesh>(null);

  useFrame((state) => {
    if (meshRef.current) {
      meshRef.current.rotation.y = state.clock.elapsedTime * speed * 0.4;
      meshRef.current.rotation.x = Math.sin(state.clock.elapsedTime * speed) * 0.3;
    }
  });

  return (
    <Float speed={speed} rotationIntensity={0.8} floatIntensity={0.8}>
      <mesh ref={meshRef} position={position} scale={scale}>
        <octahedronGeometry args={[1, 0]} />
        <meshStandardMaterial
          color="#990000"
          emissive="#220000"
          emissiveIntensity={0.4}
          roughness={0.1}
          metalness={1}
        />
      </mesh>
    </Float>
  );
};

const Particles = () => {
  const count = 100;
  const mesh = useRef<THREE.InstancedMesh>(null);
  
  const particles = useMemo(() => {
    const temp = [];
    for (let i = 0; i < count; i++) {
      temp.push({
        position: [
          (Math.random() - 0.5) * 20,
          (Math.random() - 0.5) * 20,
          (Math.random() - 0.5) * 20,
        ],
        scale: Math.random() * 0.05 + 0.02,
        speed: Math.random() * 0.5 + 0.1,
      });
    }
    return temp;
  }, []);

  useFrame((state) => {
    if (mesh.current) {
      const dummy = new THREE.Object3D();
      particles.forEach((particle, i) => {
        const t = state.clock.elapsedTime * particle.speed;
        dummy.position.set(
          particle.position[0] + Math.sin(t) * 0.3,
          particle.position[1] + Math.cos(t) * 0.3,
          particle.position[2]
        );
        dummy.scale.setScalar(particle.scale);
        dummy.updateMatrix();
        mesh.current!.setMatrixAt(i, dummy.matrix);
      });
      mesh.current.instanceMatrix.needsUpdate = true;
    }
  });

  return (
    <instancedMesh ref={mesh} args={[undefined, undefined, count]}>
      <sphereGeometry args={[1, 8, 8]} />
      <meshStandardMaterial color="#ff3333" emissive="#330000" emissiveIntensity={1} />
    </instancedMesh>
  );
};

const Scene3D = () => {
  return (
    <div className="absolute inset-0 z-0">
      <Canvas
        camera={{ position: [0, 0, 8], fov: 60 }}
        dpr={[1, 2]}
        gl={{ antialias: true, alpha: true }}
      >
        <ambientLight intensity={0.3} />
        <pointLight position={[10, 10, 10]} intensity={1} color="#ff0000" />
        <pointLight position={[-10, -10, -5]} intensity={0.5} color="#ff3333" />
        <spotLight
          position={[0, 10, 0]}
          angle={0.3}
          penumbra={1}
          intensity={1}
          color="#cc0000"
        />

        {/* Main floating shapes */}
        <FloatingShape position={[-4, 2, -2]} scale={1.2} speed={1.5} rotationSpeed={0.5} distort={0.4} />
        <FloatingShape position={[4, -1, -3]} scale={0.8} speed={2} rotationSpeed={0.8} distort={0.3} />
        <FloatingShape position={[0, 3, -4]} scale={0.6} speed={1.2} rotationSpeed={0.6} distort={0.5} />
        
        {/* Torus shapes */}
        <FloatingTorus position={[-3, -2, -1]} scale={0.5} speed={1} />
        <FloatingTorus position={[5, 1, -2]} scale={0.4} speed={1.5} />
        
        {/* Octahedron shapes */}
        <FloatingOctahedron position={[2, 2, -1]} scale={0.4} speed={0.8} />
        <FloatingOctahedron position={[-2, 0, -3]} scale={0.3} speed={1.2} />
        
        {/* Particle field */}
        <Particles />
      </Canvas>
    </div>
  );
};

export default Scene3D;
