import { useSignal } from "@preact/signals";
import { Github } from "npm:lucide-preact";

export default function Home() {
  const count = useSignal(3);
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-4xl flex flex-col">
          <h1 className="text-5xl font-bold">
            Introduce tu token de instagram
          </h1>
          <p className="py-6">
            Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda
            excepturi exercitationem quasi. In deleniti eaque aut repudiandae et
            a id nisi.
          </p>
          <button className="btn btn-primary">Get Started</button>
        </div>
        <a href="">
          <Github />
        </a>
      </div>
    </div>
  );
}
